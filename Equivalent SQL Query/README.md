Implementing one executable Hadoop MapReduce job that receives in input two .csv tables having the structure:
User: UserId, Name, DOB
Follows: UserIdFollower, UserIdFollowing
The MapReduce job needs to perform the following SQL query:
 select U.UserId, U.Name as NameFollower, F.Name as NameFollowing
 from User as U
 join Follows as F on U.UserId = F.UserId
 where F.DOB <= '2002-03-01'