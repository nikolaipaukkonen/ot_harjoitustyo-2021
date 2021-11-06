from invoke import task

@task
def test(ctx):
    ctx.run("pytest src -v")

@task
def foo(ctx):
    print("bar")