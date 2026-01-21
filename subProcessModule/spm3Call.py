import subprocess

print("Before call()")

code = subprocess.call(["ls", "/home/inayat-shah/DsaCep"])

print("After call()")
print("Exit code from call():", code)

print("\nBefore run()")

result = subprocess.run(
    ["ls", "/home/inayat-shah/DsaCep"],
    capture_output=True,
    text=True
)

print("After run()")
print("Return code from run():", result.returncode)
print("Error captured by run():", result.stderr)
