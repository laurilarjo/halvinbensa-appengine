from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll
""" Generic viewt korvasi naa
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list' : latest_poll_list})
    #template = loader.get_template('polls/index.html')
    #context = Context({
    #    'latest_poll_list' : latest_poll_list,
    #})
    #return HttpResponse(template.render(context))

def detail(request, poll_id):
    #try:
    #    p = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    p = get_object_or_404(Poll, pk=poll_id)    
    return render_to_response('polls/detail.html', {'poll' : p},
                              context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', { 'poll' : p})
"""

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/detail.html', {
                                'object' : p, 
                                'error_message' : "Et valinnu mitaan..",
                                }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
