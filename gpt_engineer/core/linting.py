import autopep8
import jsbeautifier


class Linter:
    def __init__(self):
        self.js_opts = jsbeautifier.default_options()
        self.js_opts.indent_size = 2

    def lint_python_code(self, code: str) -> str:
        """
        Lints the given Python code using autopep8.

        Parameters
        ----------
        code : str
            The Python code to be linted.

        Returns
        -------
        str
            The linted Python code.
        """
        return autopep8.fix_code(code)

    def lint_javascript_code(self, code: str) -> str:
        """
        Lints the given JavaScript code using jsbeautifier.

        Parameters
        ----------
        code : str
            The JavaScript code to be linted.

        Returns
        -------
        str
            The linted JavaScript code.
        """
        return jsbeautifier.beautify(code, self.js_opts)

    def lint_files_dict(self, files_dict: dict) -> dict:
        """
        Lints the given files dictionary. The dictionary keys are file names and the values are the file contents.
        The function supports linting for Python and JavaScript files.

        Parameters
        ----------
        files_dict : dict
            The dictionary containing file names as keys and file contents as values.

        Returns
        -------
        dict
            The dictionary containing linted file contents.
        """
        formatted_files = {}
        for file_name, file_content in files_dict.items():
            if file_name.endswith(".py"):
                formatted_files[file_name] = self.lint_python_code(file_content)
            elif file_name.endswith(".js"):
                formatted_files[file_name] = self.lint_javascript_code(file_content)
            else:
                formatted_files[file_name] = file_content
        return formatted_files