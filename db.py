from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete, func

# 데이터 베이스와 테이블 생성
engine = create_engine('sqlite:///./example.db', echo=True)
metadata = MetaData()

users = Table(
    'users', 
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

metadata.create_all(engine)

# 데이터 조회
# try:
#     with engine.connect() as conn:
#         result = conn.execute(select(users))
#         rows = result.fetchall()
#         for row in rows:
#             print(row)
# except Exception as e:
    # print(f"An error occured : {e}")


# 데이터 삽입
# with engine.connect() as conn:
#     conn.execute(insert(users).values(name="Alice", age=20))
#     conn.execute(insert(users), [
#         {
#             "name" : "Bob",
#             "age" : 30
#         },
#         {
#             "name" : "Carol",
#             "age" : 25
#         }
#     ])
#     conn.commit() # 변경사항 커밋


# 데이터 업데이트
# with engine.connect() as conn:
#     conn.execute(update(users).where(users.c.name == "Alice").values(age=36))
    
#     conn.commit() # 변경사항 커밋

# 연령 그룹별 평균 나이 계산 및 이름으로 정렬
try:
    with engine.connect() as conn:
        age_group_query = select(
            users.c.name, 
            func.avg(users.c.age).label("average_age")
        ).group_by(users.c.name).order_by(users.c.name)

        result = conn.execute(age_group_query)
        for row in result:
            print(row)
except Exception as e:
    print(f"An error occured: {e}")