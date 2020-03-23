# Notifications

Explains the civic europe specific notifications.

1. SubmitIdeaNotification
   - sent to: creator of idea
   - when: idea is submitted
   - template: civic_europe_notifications/emails/submit_idea_notification

2. SubmitJourneyNotification
   - sent to: creator of journey entry
   - when: journey entry is submitted
   - template: civic_europe_notifications/emails/submit_journey_notification

3. NotifyCreatorEmail
   - sent to: creator of idea
   - when: comment is added to that idea
   - not sent: when creator added that comment herself
   _or_
   - sent to: creator of comment
   - when: comment is added to that comment
   - not sent: when creator added that comment herself

   - template: civic_europe_notifications/emails/notify_creator

4. NotifyFollowersOnNewComment
   - sent to: followers of idea
   - when: comment or child-comment is added to idea
   - not sent to: creators of idea, even if they follow, because they will get the NotifyCreatorEmail
   - not sent to: followers who disabled the notifications
   - template: civic_europe_notifications/emails/notify_followers_new_comment

5. NotifyFollowersOnNewJourney
   - sent to: followers of idea
   - when: journey entry is added to idea
   - not sent to: creators of idea, even if they follow
   - not sent to: followers who disabled the notifications
   - template: civic_europe_notifications/emails/notify_followers_new_journey

6. NotifyFollowersOnWinner
   - sent to: followers of winning ideas
   - when: button in django-admin is clicked
   - not sent to: creators of winning ideas
   - not sent to: followers who disabled the notifications
   - template: civic_europe_notifications/emails/notify_followers_winner

7. NotifyFollowersOnShortlist
   - sent to: followers of shortlisted ideas, that did not win the community award
   - when: button 'notify shortlist' in django-admin is clicked
   - not sent to: creators of shortlisted ideas
   - not sent to: followers who disabled the notifications
   - template: civic_europe_notifications/emails/notify_followers_shortlist


8. NotifyFollowersOnCommunityAward
   - sent to: followers of shortlisted ideas, that also won the community award
   - when: button 'notify shortlist' in django-admin is clicked
   - not sent to: creators of shortlisted ideas
   - not sent to: followers who disabled the notifications
   - template: civic_europe_notifications/emails/notify_followers_community_award
