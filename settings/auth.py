AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.browserid.BrowserIDBackend',
    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
    # 'social_auth.backends.contrib.disqus.DisqusBackend',
    # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    # 'social_auth.backends.contrib.orkut.OrkutBackend',
    # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
    # 'social_auth.backends.contrib.github.GithubBackend',
    # 'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    # 'social_auth.backends.contrib.live.LiveBackend',
    # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
    # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    # 'social_auth.backends.contrib.readability.ReadabilityBackend',
    # 'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# TWITTER_CONSUMER_KEY         = ''
# TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = '474196079318905'
FACEBOOK_API_SECRET          = '9c0132c1c8c9a78d3029b10edcd0a5f8'
# LINKEDIN_CONSUMER_KEY        = ''
# LINKEDIN_CONSUMER_SECRET     = ''
# ORKUT_CONSUMER_KEY           = ''
# ORKUT_CONSUMER_SECRET        = ''
# GOOGLE_CONSUMER_KEY          = ''
# GOOGLE_CONSUMER_SECRET       = ''
# GOOGLE_OAUTH2_CLIENT_ID      = ''
# GOOGLE_OAUTH2_CLIENT_SECRET  = ''
# FOURSQUARE_CONSUMER_KEY      = ''
# FOURSQUARE_CONSUMER_SECRET   = ''
# VK_APP_ID                    = ''
# VK_API_SECRET                = ''
# LIVE_CLIENT_ID               = ''
# LIVE_CLIENT_SECRET           = ''
# SKYROCK_CONSUMER_KEY         = ''
# SKYROCK_CONSUMER_SECRET      = ''
# YAHOO_CONSUMER_KEY           = ''
# YAHOO_CONSUMER_SECRET        = ''
# READABILITY_CONSUMER_SECRET  = ''
# READABILITY_CONSUMER_SECRET  = ''

#LOGIN_URL          = '/session/'
#LOGIN_REDIRECT_URL = '/'
#LOGIN_ERROR_URL    = '/session/error'

SOCIAL_AUTH_UID_LENGTH = 223
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True


FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
)
