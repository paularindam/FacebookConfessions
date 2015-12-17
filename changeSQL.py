lines = open("cornellComments.sql").readlines()
f = open("cornellCommentEdited.sql","w")
for line in lines:
	line = line.replace("mytable(post_id,comment_id,user_name","comments(schoolid,postid,commentid,username")
	line = line.replace("user_id,time,like_count","userid,time,likecount")
        line = line.replace("message,FIELD8,FIELD9","message").replace("VALUES (","VALUES ('11',").replace(",'','')",")")
	f.write(line)
f.close()
'''
lines = open("cornellPost.sql").readlines()
f = open("cornellPostEdited.sql","w")
for line in lines:
	line = line.replace("mytable","posts").replace("type,FIELD7,FIELD8","type").replace("VALUES (","VALUES ('11',").replace(",'','')",")")
	line = line.replace("num_likes,num_comments","numlikes,numcomments")
	f.write(line)
f.close()
'''
