# from anthropic import Anthropic
# import os

# client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# try:
#     client.messages.create(
#         model="claude-3-5-opus-20241022",
#         max_tokens=10,
#         messages=[{"role": "user", "content": "test"}]
#     )
#     print("Opus is available")
# except Exception as e:
#     print("Opus not available:", e)

# print(repr(os.getenv("ANTHROPIC_API_KEY")))

from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

resp = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=20,
    messages=[{"role": "user", "content": "hello"}]
)

print(resp)

