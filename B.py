import smtplib
import logging
from email.mime.text import MIMEText

logging.basicConfig(filename="smtp_log.txt", level=logging.INFO)

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "bhargav159509@gmail.com"
password = "gsxcbynkgzfucsbn"  
receiver_email = "mahipalmaddu@gmail.com"

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)

    msg = MIMEText("""I never believed in time travel.
Not really.
I thought it was just sci-fi stuff — paradoxes, bootstrap loops, the kind of thing you’d find in late-night forums and Reddit threads.

But then it happened to me.

The first sign was small: a journal.
Black leather, battered at the edges, sitting on the bench at a train station where I wait every morning.
It had my handwriting inside.
Not just my handwriting — my words.
Whole pages describing my exact routine, down to the coffee I’d spill on my sleeve that same morning.

I laughed.
I thought it was some elaborate prank.
But the laughter died when the next page described what would happen that night.

It was true.

Every word.

And at the very end of the journal, a note:
“Don’t trust the man in the grey coat.”

I didn’t know what to make of it.
Until the next week, when a man in a grey coat sat across from me on the train.

He smiled at me like he’d been waiting.
“Do you believe in loops?” he asked.
My blood ran cold.

The next part isn’t clear.
The journal said I’d follow him, and I did.
To an abandoned building, old wiring buzzing in the walls.
He showed me a machine, humming with impossible energy.
He called it a “Temporal Gate.”

He said I built it.
Future me.
And he… was me.

Older, sharper around the eyes, but definitely me.
I wanted to run.
But he showed me scars only I knew I had.
The crooked scar on my ankle.
The faded burn mark on my wrist.

No denying it.

Then he handed me another journal.
“This is your path,” he said.
“You’ve already lived it.”

I opened it.
The first line made me dizzy:
“Tonight you kill her.”

I didn’t know who “her” was.
Not then.
But the night came, and I found myself outside an apartment I didn’t recognize.
Inside, a woman sat at a desk, typing.
She looked up, startled, as I entered.

And I froze.

Because she looked exactly like me.
Not older. Not younger.
Just… me.

Same face. Same voice.
Everything.

She whispered, “So it’s you this time.”
Like she’d been through this before.
Like she was waiting for me.

The journal burned in my hands.
The words blurred and twisted:
“You kill her, or she kills you. One loop must survive.”

I dropped the book and backed away.
But she lunged, eyes wild, hands around my throat.
She fought like me, because she was me.
Every move mirrored.
Every strike anticipated.

I don’t remember deciding.
I only remember the knife in my hand.
The scream that sounded exactly like mine.
The blood.

When it was over, I stood above her body, gasping.
The journal lay open on the floor.
New words appeared, written in fresh ink.
“Now you understand. Now you become me.”

I staggered out into the night.
And when I passed a store window, I caught my reflection.
The grey coat hung heavy on my shoulders.

I was the man I wasn’t supposed to trust.

And tomorrow, I’ll find myself on that train, asking the younger version of me if he believes in loops.

Because that’s the only way the story works.
""")
    msg["Subject"] = "The Time I Realized I Was My Own Enemy"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server.sendmail(sender_email, receiver_email, msg.as_string())
    logging.info("Email sent successfully")
    print("✅ Email sent successfully!")
    server.quit()

except Exception as e:
    logging.error(f"SMTP error: {e}")
    print("❌ Error:", e)
