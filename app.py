from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient_name = request.form['recipient_name']
        recipient_age = request.form['recipient_age']
        previous_address = request.form['previous_address']
        total_family_members = request.form['total_family_members']
        partner_name = request.form['partner_name']
        partner_age = request.form['partner_age']
        children_data = request.form.getlist('child[]')

        children = []
        for i in range(0, len(children_data), 2):
            children.append((children_data[i], children_data[i+1]))

        print("Recipient Name:", recipient_name)
        print("Recipient Age:", recipient_age)
        print("Previous Address:", previous_address)
        print("Total Family Members:", total_family_members)
        print("Partner Name:", partner_name)
        print("Partner Age:", partner_age)
        print("Children:", children)

        return redirect('/')

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
