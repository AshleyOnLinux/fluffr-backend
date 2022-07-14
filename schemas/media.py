def mediaEntity(item) -> dict:
    return {
        "isImage": item["isImage"],
        "isVideo": item["isVideo"],
        "media_id": item['media_id'],
        "filename": item["filename"],
        "base64": item["base64"],
        "author_id": item['author_id']
    }


def mediasEntity(entity) -> list:
    return [mediaEntity(item) for item in entity]
