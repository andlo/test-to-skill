from mycroft import MycroftSkill, intent_file_handler


class TestTo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('to.test.intent')
    def handle_to_test(self, message):
        self.speak_dialog('to.test')


def create_skill():
    return TestTo()

