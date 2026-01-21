import subprocess

# subprocess.run([
#     "python3",
#     "/home/inayat-shah/DsaCep/cepdGui.py"
# ])

#capture the output of commands


# result = subprocess.run(
#     ["ls", "/home/inayat-shah"],
#     capture_output=True,
#     text=True
# )

# print(result.stdout)
import subprocess

p = subprocess.Popen(
    ["ls", "-l"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

output, error = p.communicate()

print("Output:")
print(output)

print("Error:")
print(error)
