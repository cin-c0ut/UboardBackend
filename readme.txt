Booting and useful commands: 




Showing all models: 
python manage.py shell -c "from django.apps import apps; print('\n'.join([model.__name__ for model in apps.get_models()]))"

Showing views functions against viewsets: 
python manage.py shell -c "from rest_framework import viewsets; from backend.views import *; print('Custom and Overridden Methods in Viewsets:\n'); [print(f'{name}:\n' + '\n'.join([f'  - {method}' for method in dir(obj) if not method.startswith('_') and (method not in dir(viewsets.ModelViewSet) or (hasattr(getattr(obj, method), '__qualname__') and getattr(obj, method).__qualname__.startswith(name)))]) + '\n') for name, obj in globals().items() if isinstance(obj, type) and issubclass(obj, viewsets.ModelViewSet) and obj != viewsets.ModelViewSet]"
