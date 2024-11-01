from abc import ABC, abstractmethod


class InterviewService(ABC):
    @abstractmethod
    def insertSession(self):
        pass

    @abstractmethod
    def insertFirstQuestion(self):
        pass

    @abstractmethod
    def getSession(self, sessionId):
        pass

    @abstractmethod
    def getFirstQuestion(self, questionId):
        pass