import multiprocessing
from subprocess import check_output

def compute(rd, wt):
    # Read what is in the pipe1
    # This recv blocks until data is received in the pipe
    data = rd.recv()
    # Write to another pipe2
    wt.send(data.upper())

def run_cmd(rd, wt):
    cmd = rd.recv()
    wt.send(check_output(cmd).decode('ascii'))

def main():
    # Create pipes, it returns read and write descriptor of the pipe
    # i.e descriptor of reader end and writer end
    rd1, wt1 = multiprocessing.Pipe()
    rd2, wt2 = multiprocessing.Pipe()

    # Pass read end of pipe1 and write end of pipe2
    child = multiprocessing.Process(target=compute, args=(rd1, wt2))
    child.start()

    content = 'a sample string'
    # Write to pipe1
    wt1.send(content)

    # Read from pipe2
    payload = rd2.recv()

    print('send:', content)
    print('recv:', payload)
    print()
    child2 = multiprocessing.Process(target=run_cmd, args=(rd1, wt2))
    child2.start()

    # Parent sends list of commands to be executed by child
    command = ['ipconfig', '/all']
    wt1.send(command)
    # Read the output in pipe2
    output = rd2.recv()
    print ('send command: ', *command)
    print('recv output: ', output)

if __name__ == '__main__':
    main()