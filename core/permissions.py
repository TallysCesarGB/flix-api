from rest_framework.permissions import BasePermission

class GlobalDefultPermissionClass(BasePermission):
    def has_permission(self, request, view):
        # Obtém o nome do modelo da queryset da view
        model_name = view.queryset.model._meta.model_name
        app_label = view.queryset.model._meta.app_label

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            perm = f'view_{model_name}'
        elif request.method == 'POST':
            perm = f'add_{model_name}'
        elif request.method in ['PUT', 'PATCH']:
            perm = f'change_{model_name}'
        elif request.method == 'DELETE':
            perm = f'delete_{model_name}'
        else:
            return False
        
        full_perm = f'{app_label}.{perm}'
        return request.user.has_perm(full_perm)