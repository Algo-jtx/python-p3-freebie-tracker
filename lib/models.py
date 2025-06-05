from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')

    def __repr__(self):
        return f'<Company {self.name}>'
    
    def get_freebies(self): 
        return self.freebies

    def devs(self):
        unique_devs = {freebie.dev for freebie in self.freebies}
        return list(unique_devs)
    
    def give_freebie(self, dev_instance, item_name, value):
        raise NotImplementedError("give_freebie method not yet implemented.")

    
    @classmethod
    def oldest_company(cls, session_instance):
        raise NotImplementedError("oldest_company method not yet implemented.")



class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', backref='dev')


    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def get_freebies(self): 
        return self.freebies

    def companies(self):
        unique_companies = {freebie.company for freebie in self.freebies}
        return list(unique_companies)
    
    def received_one(self, item_name):
        raise NotImplementedError("received_one method not yet implemented.")

    def give_away(self, target_dev, freebie_instance):
        raise NotImplementedError("give_away method not yet implemented.")

    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)

    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)

    def __repr__(self):
        return f'<Freebie: {self.item_name} (Value: ${self.value}) from {self.company.name} owned by {self.dev.name}>'

    def get_dev(self):
        return self.dev

    def get_company(self):
        return self.company
    
    def print_details(self):
        raise NotImplementedError("print_details method not yet implemented.")
