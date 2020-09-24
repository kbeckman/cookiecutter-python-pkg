# pylint: disable=no-self-use, missing-docstring, protected-access

import {{ cookiecutter.package_slug }}

class TestEchoHello:
    def test_a_useless_test(self):
        pass

    def test_returns_text(self):
        subject = {{ cookiecutter.package_slug }}.HelloWorld()

        assert subject.echo_hello() == "hello, world!"
