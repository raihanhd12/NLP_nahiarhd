from nahiarhdNLP.preprocessing.main import Pipeline


def test_pipeline_config_mode_main():
    config = {"clean_html": True, "clean_mentions": True, "remove_urls": True}
    pipe = Pipeline(config)
    text = "Hello <b>World</b> @User https://EXAMPLE.com"
    result = pipe.process(text)

    # HTML tags should be removed
    assert "<" not in result and ">" not in result

    # mentions removed
    assert "@" not in result

    # urls removed
    assert "http" not in result and "https" not in result


def test_update_config_and_get_enabled_steps_and_repr():
    config = {"clean_html": True, "clean_mentions": False}
    pipe = Pipeline(config)

    assert pipe.get_enabled_steps() == ["clean_html"]

    pipe.update_config({"clean_mentions": True})
    enabled = pipe.get_enabled_steps()
    assert "clean_mentions" in enabled
    assert "clean_html" in enabled

    assert "Pipeline(config=" in repr(pipe)


def test_pipeline_process_empty_returns_empty():
    pipe = Pipeline({})
    assert pipe.process("") == ""
