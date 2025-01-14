import sys
import unittest

from huggingface_hub.file_download import is_tf_available


def require_tf(test_case):
    """
    Decorator marking a test that requires TensorFlow.

    These tests are skipped when TensorFlow is not installed.

    """
    if not is_tf_available():
        return unittest.skip("test requires Tensorflow")(test_case)
    else:
        return test_case


@require_tf
def test_import_huggingface_hub_doesnt_import_tensorfow():
    # `import huggingface_hub` is not necessary since huggingface_hub is already imported at the top of this file,
    # but let's keep it here anyway just in case
    import huggingface_hub  # noqa

    assert "tensorflow" not in sys.modules
