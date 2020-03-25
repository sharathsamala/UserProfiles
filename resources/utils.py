

def profile_to_json(profile):

    data = {
            'username': profile.username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'email_id': profile.email_id,
            'profile_img': profile.profile_img,
            'about_me': profile.about_me,
            'resume': profile.resume,
            'enabled_sections': profile.enabled_sections,
            'phone': phone_to_json(profile.phone)
        }

    return data


def phone_to_json(phone):

    data = {
            'country_code': phone.country_code,
            'primary': phone.primary,
            'secondary': phone.secondary
        }

    return data
