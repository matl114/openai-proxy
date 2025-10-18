import databases

from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database config
DATABASE_URL = 'sqlite:///./openai_log.db'
database = databases.Database(DATABASE_URL)
Base = declarative_base()


# database model
class OpenAILog(Base):
    """
    OpenAI API call log
    """
    __tablename__ = 'openai_logs'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # request url
    request_url = Column(String)
    # request method
    request_method = Column(String)
    # request time, timestamp in millisecond
    request_time = Column(BigInteger)
    # response duration, in seconds
    response_duration = Column(BigInteger)
    # response status code
    status_code = Column(Integer)
    # request content
    request_content = Column(String)
    # response header
    response_header = Column(String)
    # response content
    response_content = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'request_url': self.request_url,
            'request_method': self.request_method,
            'request_time': self.request_time,
            'response_duration': self.response_duration,
            'status_code': self.status_code,
            'request_content': self.request_content,
            'response_header': self.response_header,
            'response_content': self.response_content,
        }


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def save_log(log: OpenAILog):
    async with database.transaction():
        query = OpenAILog.__table__.insert().values(**log.to_dict())
        await database.execute(query)
