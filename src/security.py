import os

# Very simple security
# Checks if the header has a (not super secret) secret key
def security_check(request):
  return request.headers.get("X-SECRET-APP-KEY") == os.getenv("SECRET_APP_KEY")