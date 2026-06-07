from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://root:MySQL%40Root%232026@localhost/devana_estimator"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
from sqlalchemy import text

def save_estimate(project_name, area, total_cost, cement, steel, bricks):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO estimates
                (project_name, area, total_cost, cement, steel, bricks)
                VALUES
                (:project_name, :area, :total_cost, :cement, :steel, :bricks)
            """),
            {
                "project_name": project_name,
                "area": area,
                "total_cost": total_cost,
                "cement": cement,
                "steel": steel,
                "bricks": bricks
            }
        )
        conn.commit()