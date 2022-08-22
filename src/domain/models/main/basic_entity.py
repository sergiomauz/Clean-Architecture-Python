"""
    ToDo: DocString
"""
import uuid
import datetime
from typing import List
from sqlalchemy.dialects.postgresql import UUID as pg_uuid
from domain.persistence.main import sql_alchemy as db
from common.utils import convert_to_uuid
from application.common.general import BasicSearchParameters


class BasicEntity(db.Model):
    """ ToDo: DocString """
    __abstract__ = True
    uid = db.Column(pg_uuid(as_uuid = True), primary_key = True, default = uuid.uuid1())
    created_at = db.Column(db.DateTime, nullable = False)
    modified_at = db.Column(db.DateTime, nullable = True)

    @classmethod
    def get_by_uid(cls, str_uid: str):
        """ ToDo: DocString """
        uid = convert_to_uuid(str_uid)

        if uid is not None:
            try:
                return cls.query.get(uid)
            except Exception:
                return None

        return None

    @classmethod
    def get_list_by_uids(cls, uids_list: List[str]):
        """ ToDo: DocString """
        return cls.objects.filter(uid__in = uids_list)

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        page_size = basic_search_parameters.page_size
        offset = (basic_search_parameters.current_page - 1) * basic_search_parameters.page_size

        return cls.objects.filter(uid__icontains =
                                    basic_search_parameters.filter_value
                                    ).order_by(
                                        "-created_at", "-modified_at"
                                    )[offset : offset + page_size]

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.objects.filter(uid__icontains =
                                    basic_search_parameters.filter_value).count()

    def save(self):
        """ ToDo: DocString """
        if self.uid is None:
            self.uid = uuid.uuid1()
            self.created_at = datetime.datetime.now()
            db.session.add(self)
        else:
            self.modified_at = datetime.datetime.now()
            db.session.merge(self)
        db.session.commit()
