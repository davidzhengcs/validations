#!/usr/bin/env python3

def validate_user(username, minlen):
  """Checks if the recieved ussername matches the required conditions."""
  if type(username) != str:
    raise TypeError("username must be a string")
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
  if len(username) < minlen:
    return Flase
  return True
