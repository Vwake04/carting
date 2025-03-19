import logging

from sqlalchemy.exc import ProgrammingError

from src.database import engine, Base, SessionLocal
from src.models import Item, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db() -> None:
    """Initialize the database with tables and initial data."""
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully")

        # Add initial data if needed
        db = SessionLocal()
        try:
            # Check if we already have items
            item_count = db.query(Item).count()

            if item_count == 0:
                # Add sample items
                sample_items = [
                    Item(name="Sample Item 1", description="This is a sample item"),
                    Item(
                        name="Sample Item 2", description="This is another sample item"
                    ),
                    Item(
                        name="Sample Item 3",
                        description="This is yet another sample item",
                    ),
                ]
                db.add_all(sample_items)
                db.commit()
                logger.info("Added sample items")
            else:
                logger.info(f"Database already contains {item_count} items")

            # Check if we already have users
            # user_count = db.query(User).count()

            # if user_count == 0:
            #     # Add sample users
            #     sample_users = [
            #         User(name="User 1"),
            #         User(name="User 2"),
            #         User(
            #             name="User 3", acquired_item=1
            #         ),  # Assumes item with ID 1 exists
            #     ]
            #     db.add_all(sample_users)
            #     db.commit()
            #     logger.info("Added sample users")
            # else:
            #     logger.info(f"Database already contains {user_count} users")

        finally:
            db.close()

    except ProgrammingError as e:
        logger.error(f"Error initializing database: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")
