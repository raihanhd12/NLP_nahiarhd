from nahiarhdNLP.preprocessing import Pipeline

config = {"clean_html": True, "clean_mentions": True, "remove_urls": True}
pipe = Pipeline(config)
print("enabled:", pipe.get_enabled_steps())
print("functions count:", len(pipe.functions))
print("output:", pipe.process("Hello <b>World</b> @User https://EXAMPLE.com"))
