from app.extensions import db
from app.models import Course, Lesson, Module


def seed_sample_course() -> Course:
    course = Course.query.filter_by(slug="bridge-bidding-foundations").first()
    if course is None:
        course = Course(slug="bridge-bidding-foundations")
        db.session.add(course)

    course.title = "Bridge Bidding Foundations"
    course.summary = "A calm, structured starting point for players learning core bidding conversations."
    course.description = (
        "Build confidence with the ideas behind opening bids, responder structure, and the decision-making "
        "habits that make partnerships more accurate."
    )
    course.sort_order = 1
    course.is_published = True

    module = Module.query.filter_by(slug="1nt-opening-and-responses").first()
    if module is None:
        module = Module(slug="1nt-opening-and-responses", course=course)
        db.session.add(module)

    module.course = course
    module.title = "1NT Opening and Responses"
    module.summary = "Learn what a 1NT opening promises and how responder can steer the auction."
    module.sort_order = 1

    lessons = [
        {
            "slug": "what-a-1nt-opening-shows",
            "title": "What a 1NT Opening Shows",
            "summary": "Understand the balanced shape and point range behind the opening bid.",
            "sort_order": 1,
            "body": (
                "A natural 1NT opening usually shows a balanced hand in a narrow high-card point range. "
                "That precision helps responder judge whether the partnership belongs in partscore, game, "
                "or a slam investigation.\n\n"
                "When you open 1NT, you are telling partner about strength and shape in a single call. "
                "That is why disciplined ranges matter so much in notrump systems.\n\n"
                "Practice focus: compare a flat 15-count with a semi-balanced 17-count and ask whether "
                "both belong in the same opening range."
            ),
        },
        {
            "slug": "stayman-after-1nt",
            "title": "Using Stayman After 1NT",
            "summary": "See how responder asks for a four-card major and plans the next rebid.",
            "sort_order": 2,
            "body": (
                "Stayman is responder's tool for locating a 4-4 major-suit fit after partner opens 1NT. "
                "The 2C response asks opener whether they hold a four-card major.\n\n"
                "Responder should use Stayman with a clear follow-up plan. Sometimes the goal is to stop "
                "in two of a major, and sometimes the goal is to invite or force game after finding a fit.\n\n"
                "Auction context: 1NT - 2C - 2H. What kinds of responder hands continue with 3H, 4H, "
                "or 2NT?"
            ),
        },
        {
            "slug": "jacoby-transfers-over-1nt",
            "title": "Jacoby Transfers Over 1NT",
            "summary": "Use transfer bids to place the stronger hand as declarer and describe major-suit length.",
            "sort_order": 3,
            "body": (
                "Jacoby transfers let responder show a five-card or longer major while keeping opener as "
                "the likely declarer. After 1NT, 2D transfers to hearts and 2H transfers to spades.\n\n"
                "Transfers improve declarer placement and keep the notrump opener hidden from the opening lead. "
                "They also create room for invitational and game-forcing continuations.\n\n"
                "Hand diagram prompt: imagine responder holds five hearts and invitational values. What is the "
                "difference between transferring and then inviting versus jumping directly?"
            ),
        },
        {
            "slug": "invitational-and-game-going-choices",
            "title": "Invitational and Game-Going Choices",
            "summary": "Learn how responder distinguishes between partscore, invite, and game after 1NT.",
            "sort_order": 4,
            "body": (
                "After a 1NT opening, responder often decides among signoff, invitational, and game-going actions. "
                "The choice depends on point count, fit, texture, and whether a major-suit contract may play better.\n\n"
                "Strong bidding is not only about counting points. It also means visualizing tricks, stoppers, and "
                "whether notrump or a major will score more safely.\n\n"
                "Multiple-choice preview: with 8 points and a balanced hand, when should responder invite with 2NT "
                "instead of forcing to game?"
            ),
        },
    ]

    for lesson_data in lessons:
        lesson = Lesson.query.filter_by(slug=lesson_data["slug"]).first()
        if lesson is None:
            lesson = Lesson(slug=lesson_data["slug"], module=module)
            db.session.add(lesson)

        lesson.module = module
        lesson.title = lesson_data["title"]
        lesson.summary = lesson_data["summary"]
        lesson.body = lesson_data["body"]
        lesson.sort_order = lesson_data["sort_order"]
        lesson.is_published = True

    db.session.commit()
    return course
