from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask


def config_doc_spec(app: Flask):
    spec = APISpec(
        title='My Flask RESTFUL Sample APP',
        info=dict(description="Show how easy is to create a gateway API with documentation"),
        version='0.1.0',
        openapi_version='2.0.0',
        plugins=[MarshmallowPlugin()],
    )

    app.config.update({
        'APISPEC_SPEC': spec,
        'APISPEC_SWAGGER_URL': '/openapi.json',  # URI to access API Doc JSON
        'APISPEC_SWAGGER_UI_URL': '/docs/'  # URI to access UI of API Doc
    })
