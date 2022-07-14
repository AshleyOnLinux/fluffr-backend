def userEntity(item) -> dict:
    return {
        "account_id": item["account_id"],
        "nickname": item["nickname"],
        "handle": item['handle'],
        "email": item["email"],
        "password": item["password"],

        "social_links": item['social_links'],
        "awards": item['awards'],
        "roles": item['roles']

    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
