from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship

from domain.league import League

metadata = MetaData()

league_data = Table(
    "leagues",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100)),
    Column("country", String(100), nullable=False),
    Column("starting_date", Date),
    Column("ending_date", Date),
    Column("country_flag", String(255)),
    Column("league_flag", String(255)),

)


# batches = Table(
#     "batches",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("reference", String(255)),
#     Column("sku", String(255)),
#     Column("_purchased_quantity", Integer, nullable=False),
#     Column("eta", Date, nullable=True),
# )
#
# allocations = Table(
#     "allocations",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("orderline_id", ForeignKey("order_lines.id")),
#     Column("batch_id", ForeignKey("batches.id")),
# )


def start_mappers():
    mapper(League, league_data)
    # mapper(
    #     League,
    #     league_data,
    #     # properties={
    #     #     "_allocations": relationship(
    #     #         lines_mapper, secondary=allocations, collection_class=set,
    #     #     )
    #     # },
    # )
