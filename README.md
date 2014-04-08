# Livefyre Python Utility Classes
[![PyPI version](https://badge.fury.io/py/livefyre.png)](http://badge.fury.io/py/livefyre)

Livefyre's official library for common server-side tasks necessary for getting Livefyre apps (comments, reviews, etc.) working on your website.

Works with Python versions: 2.6, 2.7, 3.2, 3.3

## Installation

Run this line:

    $ pip install livefyre

## Usage

Instantiating a network object:

```python
network = Livefyre.get_network('network_name', 'network_key')
```

Building a Livefyre token:

```python
network.build_livefyre_token()
```

Building a user auth token:

```python
network.build_user_auth_token('user_id', 'display_name', expires)
```

To validate a Livefyre token:

```python
network.validate_livefyre_token('lf_token')
```

To send Livefyre a user sync url and then have Livefyre pull user data from that url:

```python
network.set_user_sync_url('url_template')
network.sync_user('user_id')
```

Instantiating a site object:

```python
site = network.get_site('site_id', 'site_key')
```

Building a collection meta token:
*The 'tags' and stream' arguments are optional.*

```python
site.build_collection_meta_token('title', 'article_id', 'url', 'tags', 'stream')
```

Building a checksum:
*The 'tags' argument is optional.*

```python
site.build_checksum('title', 'url', 'tags')
```

To retrieve content collection data:

```python
site.get_collection_content('article_id')
```

To get a content collection's id:

```python
site.get_collection_id('article_id')
```

## Documentation

Located [here](http://answers.livefyre.com/developers/libraries).

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

Note: any feature update on any of Livefyre's libraries will need to be reflected on all libraries. We will try and accommodate when we find a request useful, but please be aware of the time it may take.

## License

MIT