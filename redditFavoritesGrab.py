import praw
import prawcore
import os

def reddit_login():
    '''logs in the user using OAuth 2.0 and returns a redditor object for use'''
    user_agent = 'PC:redditFavoriteGrab:v0.1 (by /u/Scien)'
    r = praw.Reddit('mysettings', user_agent=user_agent)
    try:
        return r.user.me()
    except prawcore.exceptions.Forbidden:
        print('\nIt seems your credentials are invalid. Please check whether your praw.ini file is properly setup.')
        return None


def main():
    if os.path.isfile('./redditFavorites.txt'):
        print('Please delete or move your current redditFavorites.txt to a safe place.')
        return # exit the script if file problems

    file = open('redditFavorites.txt','w')

    redditor = reddit_login()
    if redditor is None:
        print('\nStopping script...')
        return  # exit the script if unable to log in to reddit 

    print('Welcome /u/{}. I will help you backup your saved posts on reddit :)'.format(redditor))
    saved = redditor.saved(limit=None)

    saved_posts = []
    saved_comments = []

    for post in saved:  # separate out posts and commets
        if isinstance(post, praw.models.Submission):
            saved_posts.append(post)
        elif isinstance(post, praw.models.Comment):
            saved_comments.append(post)

    for post in saved_posts:
        # There is probably a better way to handle encoding here.  I was failing in win due to console encoding differences.
        file.write('[{0!a}] {1!a} - {2!a}\n'.format(post.shortlink, post.title, post.url))
        
    print('Done creating a list of posts...')

    for comment in saved_comments:
        comment_url = comment.link_url + comment.id
        file.write('[{0!a}] - Comment\n'.format(comment_url))
        
    print('Done creating a list of comments...')

    file.close()
    
if __name__ == '__main__':
    main()
