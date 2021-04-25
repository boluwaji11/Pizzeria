from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pizza, Topping
from .forms import CommentForm

# Create your views here.


def index(request):
    return render(request, "pizzas/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("name")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("name")

    # List of active comments for this pizza
    comments = pizza.comments.filter(active=True)

    new_comment = None

    if request.method != "POST":
        comment_form = CommentForm()
    else:
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create Comment object but doesn't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current pizza to the comment
            new_comment.pizza = pizza
            # Save the comment to the database
            new_comment.save()
            messages.success(request, "Your comment has been added successfully!")
            return redirect("pizzas:pizza", pizza_id=pizza_id)

    context = {
        "pizza": pizza,
        "toppings": toppings,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }

    return render(request, "pizzas/pizza.html", context)
