#Εισάγουμε το framework flask
from flask import Flask,render_template,request,session,g,url_for,redirect

# Δημιουργούμε μια λίστα που περιέχει μικρότερες
# λίστες με τα στοιχεία του κάθε χρήστη.
# Αρχικοποιούμε τη λίστα users:
users= []
# Με την append() προσθέτουμε κάθε χρήστη ως
# μια μικρότερη λίστα αποτελούμενη από τρία πεδία. 
# Το πρώτο πεδίο αφορά ένα μοναδικό αριθμό (user id).
# Το δεύτερο πεδίο αφορά το όνομα του χρήστη (username).
# Τέλος, το τρίτο αφορά τον κωδικό του χρήστη (password)
users.append([1, 'Giannis','12345'])
users.append([2, 'Maria','23456'])


#Δίνουμε το όνομα app στο flask
app = Flask(__name__)
app.secret_key = "secret_key"

@app.before_request
def before_request():
    # Αρχικοποιούμε το αντικείμενο g.user:
    g.user=None
    # Ελέγχουμε αν είναι κατειλημμένο το session cookie,
    # αν δηλαδή έχει συνδεθεί ο χρήστης.
    if 'user_id' in session:
        # Διατρέχουμε τη λίστα των χρηστών, ώστε να εντοπίσουμε σε ποιον ανήκει 
        # ο μοναδικός αριθμός που είναι αποθηκευμένος στο session cookie.
        for user in users:
            if user[0] == session['user_id']:
                # Αποθηκεύουμε τη λίστα που αφορά τα στοιχεία του χρήστη 
                # στο g.user, ώστε να είναι προσβάσιμα από όλες τις σελίδες.
                g.user = user

# H @app.route() της βιβλιοθήκης Flask  εκτελεί τη συνάρτηση που ακολουθεί, 
# ανάλογα με τη διευθυνση URL που επισκέπτεται ο χρήστης
@app.route('/')
def hello_world():
    return 'Hello World!'


# Χρησιμοποιούμε το όρισμα methods για να δηλώσουμε ότι
# μπορούμε να δεχθούμε δεδομένα από τη φόρμα μας.
@app.route('/logme', methods=['POST','GET'])
def logme():
    # Μόλις ένας χρήστης επισκέπτεται τη σελίδα login
    # αφαιρούμε το τυχόν session cookie που έχει 
    # αποθηκευτεί στον υπολογιστή του χρήστη.
    # Το πετυχαίνουμε αυτό με τη session.pop:
    session.pop('user_id', None)
    # Τα περιεχόμενα της παρακάτω if θα εκτελεστούν όταν ο 
    # χρήστης επιλέξει το κουμπί ΕΙΣΟΔΟΣ.
    if request.method=='POST':
        # Αποθηκεύουμε το username και τον κωδικό
        # από το χρήστη που συμπλήρωσε τη φόρμα.
        username = request.form['username']
        password = request.form['password']
        for user in users:
           # Διατρέχουμε τη λίστα των χρηστών για να ελέγξουμε αν υπάρχει
           # χρήστης σύμφωνα με τα στοιχεία που λάβαμε από την φόρμα:
            if user[1]==username and user[2]==password:
                # Αν τα στοιχεία που έχει δώσει ο χρήστης είναι σωστά,
                # τότε δημιουργούμε ένα session cookie με όνομα user_id
                # και αποθηκεύουμε εκεί το μοναδικό αριθμό που αντιστοιχεί
                # στο χρήστη.
                session['user_id'] = user[0]
                # Έπειτα δρομολογούμε το χρήστη στη σελίδα που θα 
                # είναι διαθέσιμα τα δεδομένα του sense HAT.
                return redirect(url_for('sense_data'))
    return render_template('login.html')

@app.route('/sense')
def sense_data():
    if not g.user:
        return redirect(url_for('logme'))
    return render_template('info.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
