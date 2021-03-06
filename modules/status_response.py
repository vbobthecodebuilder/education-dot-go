from send import send_sms
# TODO: query the status of this phone number

users = {
    '+14088288498': ['Vibhav', 1, 1, False],
    '+15133311772': ['Rajat', 1, 1, False],
    '+16177101266': ['Parker', 1, 1, False],
    '+18324836840': ['Anushree', 1, 1, False],
    '+14054036409': ['Joseph', 2, 1, False]
}

courses = {
    0: 'new user',
    1: 'Sex Education All Ages',
    2: 'Introduction to Math Age 11-13',
    3: 'Intermediate Math Age 13-15',
    4: 'Advanced Math Age 15-17',
    5: 'Introduction to Biology Age 11-13',
    6: 'Advanced Biology Age 13-15',
    7: 'Introduction to Chemistry Age 11-13'
}

lessons = {
    'sex_ed': {
        0: ("Lesson 1: Welcome to Sexual Education 101! We're very excited to have you and to help you understand your body and empower you to make safe, healthy sexual decisions. For our first course we'll be talking about the parts of the female reproductive system. The female reproductive system is comprised of three major parts: the vagina, the cervix, and the uterus. The vagina is a hollow tube that extends from the external opening to the cervix (the vulva is the very outside portion); the vulva contains the clitoris, and the urethera where urine is passed. The uterine lining is an inner part of the body that is shed during your menstrual cycle - we'll discuss this in lesson 5! The uterus is where the baby develops after intercourse (discussed in lesson 4). The ovaries connect the uterus to the fallopian tubes and this is where the female reproductive hormones--namely estrogen--are released during puberty.", '')
    },
    'math': {}
}

quiz_content = {
    
}

def get_user_info(phone_num):
    val = users[phone_num]
    name = val[0]; class_num = val[1];  course_num = val[2]; taking_quiz = val[3]
    global name; global class_num; global course_num; global taking_quiz

# status = '1.2'
# taking_quiz = False

def transition(phone_num, body):
    get_user_info(phone_num)
    if taking_quiz:
        ans_verify(phone_num, body)
    else:
        body_split = body.lower().split()
        message = body_split[0]
        if message == 'help':
            help(phone_num)
        elif message == 'progress':
            progress(phone_num)
        elif message == 'resume':
            resume(phone_num)
        elif message == 'test' or message == 'exam' or message == 'quiz':
            quiz(phone_num)


def not_in_db(phone_num):
    send_sms(phone_num,
             'Sorry this phone number is currently not registered in our database. Please contact a local refugee camp manager to sign up :)')

def in_db(phone_num):
    send_sms(phone_num,
             'Hi! Welcome to Education.Go, an on-the-go education system. To see all the courses that are available, type "C". If you need help, type "HELP". To return to the home text, type HOME.')

def progress(phone_num):
    send_sms(phone_num,
             'Current progress is at %s class number %s' % (courses[course_num], class_num))

def help(phone_num):
    assist = '+16177101267'
    send_sms(phone_num,
             'Please contact this number for furthuer assistance: %s' % assist)

def resume(phone_num):
    to_send = query_class_content(course_num + 1, class_num + 1) # TODO: query the class information
    send_sms(phone_num, to_send)

def quiz(phone_num):
    to_send = query_quiz_content(course_num + 1, class_num + 1) #
    send_sms(phone_num, to_send)

def ans_verify(phone_num, message):
    # TODO: set taking_quiz = False
    # TODO: query the answers
    if ans.lower() != message.lower():
        send_sms(phone_num, 'Sorry the answer was incorrect')
    else:
        send_sms(phone_num, 'Congratulations! You have entered the correct answer :)')
        # TODO: update the status of the phone number in db







