import facebook


graph = facebook.GraphAPI(access_token="Your Access", version="2.1")
post = graph.get_object(id='992333717455901', fields='name')
print(post['name'])

