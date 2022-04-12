from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/ui/the_ui.py", pty=True)