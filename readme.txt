Booting and useful commands: 




Showing all models: 
python manage.py shell -c "from django.apps import apps; print('\n'.join([model.__name__ for model in apps.get_models()]))"

Showing views functions against models: 
python manage.py shell -c "from backend.views import ClimbViewSet; print('\n'.join([method for method in dir(ClimbViewSet) if not method.startswith('_')]))"
