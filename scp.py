import pexpect

host = "127.0.0.1"
remote_path = "/"
local_path = "/"
file = "file"

user = "user"
password = "pass"

command = "scp -r %s@%s:%s/%s %s" % (user, host, remote_path, file, local_path) 

child = pexpect.spawn(command)
child.expect('pasword:')
child.sendline(password)
child.expect(pexpect.EOF)
print child.before