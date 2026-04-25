def require_auth(func):
    
    def wrapper(user):
        if user.lower() == 'admin':
            return func(user)
        elif user.lower() =='supervisor':
            return func(user)
        else:
            return "Acceso denegado"
        
    return wrapper
def admin_dashboard(user):
    return f'Bienvenido al panel, {user}'

auth_view_dashboard = require_auth(admin_dashboard)
print(auth_view_dashboard('Admin'))
print(auth_view_dashboard('Supervisor'))
print(auth_view_dashboard('andres'))


def require_auth(func):
    def wrapper(user):
        if user.lower() == 'admin':
            return func(user)
        else:
            return "Acceso denegado"
        
    return wrapper
@require_auth
def admin_dashboard(user):
    return f'Bienvenido al panel, {user}'

print(admin_dashboard(Admin))