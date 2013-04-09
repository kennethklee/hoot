import os
import logging

from django.conf import settings 
from django.shortcuts import render

from django.utils import simplejson as json
import urllib

class RestHandler():
  """
    Page handler for rendering resources. This is perfect for forms.
  
    Usage:
      Url route: ('/resource/?(.*)', ResourcesHandler)
      
      GET /resources/             ->    index(self, *args)
      GET /resources/{key}        ->    show(self, *args)
      GET /resources/new          ->    new(self, *args)
      POST /resources/new         ->    create(self, *args)
      PUT /resources/{key}        ->    update(self, *args)
      DELETE /resources/{key}     ->    destroy(self, *args)
  """
  action = 'index'

  def render(self, template_name, template_values={}):
    logging.info('=========================================')
    logging.info(unicode(self))
    logging.info(self.action)
    host_url = self.request.host_url
    values = {
      'request': self.request,
      'version': os.environ['CURRENT_VERSION_ID'],
      'action': self.action,
      'handler': unicode(self),
    }
    values.update(template_values)
  
    # template = jinja_environment.get_template(template_name)
    # self.response.out.write(template.render(values))
    return render(request, template, values)
    
  
  def get(self, *args, **kwargs):
    if len(args) > 0 and args[-1] != '':
      if args[-1] == 'new':
        self.action = 'new'
        self.new(*args, **kwargs)
      else:
        self.action = 'show'
        self.show(*args, **kwargs)
      
    else:
      self.index(*args, **kwargs)
      

  def post(self, *args, **kwargs):
    if len(args) > 0 and args[-1] != '':
      if args[-1] == 'new':
        self.action = 'new'
        self.create(*args, **kwargs)
      else:
        self.action = 'update'
        self.update(*args, **kwargs)
      
    else:
      # Should be a bad request
      self.index(*args, **kwargs)
      

  def put(self, *args, **kwargs):
    arg_length = len(args)
    if len(args) > 0 and args[-1] != '':
      action = args[-1]
      if action == 'new':
        self.action = 'new'
        self.create(*args, **kwargs)
      else:
        self.action = 'update'
        self.update(*args, **kwargs)
      
    else:
      # Should be a bad request
      self.index(*args, **kwargs)
      

  def delete(self, *args):
    if len(args) > 0 and args[-1] != '':
      self.action = 'destroy'
      self.destroy(*args, **kwargs)

  
  def index(self):
    pass
  
  def new(self, *args, **kwargs):
    pass

  def create(self, *args, **kwargs):
    pass
  
  def show(self, *args, **kwargs):
    pass
  
  def update(self, *args, **kwargs):
    pass
  
  def destroy(self, *args, **kwargs):
    pass
    
  def __unicode__(self):
    return "rest handler"
