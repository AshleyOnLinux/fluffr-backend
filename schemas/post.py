def postEntity(item) -> dict:
    return {
        "author_id": item["author_id"],
        "postTitle": item["postTitle"],
        "postTextContent": item['postTextContent'],
        "containsMedia": item['containsMedia'],
        "comments": item['comments'],
        "likes": item['likes'],
        "bookmarks": item['bookmarks'],
        "mediaID": item['mediaID'],
        "post_id": item['post_id'],
        "awards": item["awards"],
        "flair": item["flair"]

    }


def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]
