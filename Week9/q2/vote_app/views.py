from django.shortcuts import render, redirect
from .forms import VoteForm
from .models import Vote

def vote_view(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vote_result')
    else:
        form = VoteForm()

    return render(request, 'vote_app/vote.html', {'form': form})

def vote_result(request):
    total_votes = Vote.objects.count()

    good_votes = Vote.objects.filter(vote_choice='Good').count()
    satisfactory_votes = Vote.objects.filter(vote_choice='Satisfactory').count()
    bad_votes = Vote.objects.filter(vote_choice='Bad').count()

    good_percentage = (good_votes / total_votes) * 100 if total_votes else 0
    satisfactory_percentage = (satisfactory_votes / total_votes) * 100 if total_votes else 0
    bad_percentage = (bad_votes / total_votes) * 100 if total_votes else 0

    return render(request, 'vote_app/vote_result.html', {
        'good_percentage': good_percentage,
        'satisfactory_percentage': satisfactory_percentage,
        'bad_percentage': bad_percentage,
        'good_votes': good_votes,
        'satisfactory_votes': satisfactory_votes,
        'bad_votes': bad_votes,
        'total_votes': total_votes
    })


