# whatsapp-message-counter
This simple script counts the number of messages sent by all the participants in a Whatsapp group

Exported chat data from Whatsapp group is taken as the input. The phone numbers of all the active members are extracted and stored in a list. Furthermore, the script searches for the number of messages that each member has sent in the group. At last, the program returns a set of dictionary in which data is stored as "ContactName : msgcount" pair.

The script also returns the name of the contact that has sent the most number of messages in the group. Now, you know who's the spammer in your group. :p

Note: The script does not count stickers as messages. This is because exported whatsapp chat does not include stickers.
The exported chat must be renamed as "data.txt" and should be stored in the same directory as the script.

<h3>Dummy Output</h3>
<strong>python3 counter.py</strong> <br>
Output :- {'Sample ': 2, 'Sample Contact Name ': 7, 'Sample Contact ': 1, 'Sample Name ': 4, 'Contact Name ': 4}

Sample Contact Name  is the spammer in this group with  7 messages.
