# 🗣️ Behavioral Interview Tips

Technical questions test what you know; behavioral questions test how you work — and for junior roles they often matter just as much.
Everything you've built in this repo is real material: bugs fixed, things shipped, lessons learned.

---

## The STAR Method

**STAR** is a recipe for answering behavioral questions without rambling:

| Letter | Means | Ask yourself |
|--------|-------|--------------|
| **S** — Situation | Set the scene in 1-2 sentences | Where was I, what was I building? |
| **T** — Task | What specifically needed solving | What was broken, hard, or at stake? |
| **A** — Action | What *you* did, step by step | What did I try, decide, and why? |
| **R** — Result | How it ended, what you learned | Did it work? What changed after? |

Two rules of thumb: **spend most of your time on A**, and **always land the R** — a story with no result sounds like the problem is still open.

### A worked example, straight from this repo

**Question:** *"Tell me about a bug that was hard to track down."*

The [chat server](../../Projects/09_chat_server/README.md) runs one thread per
client, and every thread reads and writes the same shared `self.clients`
dictionary. Retold with STAR:

> **Situation:** "I built a multi-client chat server in Python — TCP sockets, one
> thread per connected client, all tracked in one shared dictionary."
>
> **Task:** "Under load it crashed intermittently with
> `RuntimeError: dictionary changed size during iteration` — the broadcast loop
> walked the dictionary while a disconnect thread deleted from it. Two clients,
> no problem; five clients, crash."
>
> **Action:** "The traceback pointed at the broadcast loop, and every client
> handler touches that dictionary — so it was a shared-state problem, not a
> socket problem. I guarded the dictionary with a `threading.Lock` so reads and
> writes can't overlap, and iterated over a snapshot copy of the keys so a
> disconnect mid-broadcast can't change the list under me."
>
> **Result:** "The crash stopped reproducing, and I took away a habit: when a
> structure is shared between threads, the first question is *who guards it*."

That's about a minute spoken — and the **R** includes what you learned, the part interviewers remember. The pattern, in code:

```python
import threading

class ChatServer:
    def __init__(self):
        self.clients = {}                # shared: socket -> client info
        self._lock = threading.Lock()    # ONE lock guards self.clients

    def broadcast(self, message):
        with self._lock:                 # block writers while we scan
            for sock in list(self.clients):   # snapshot of the keys
                sock.send(message.encode("utf-8"))
```

Both halves matter: the lock blocks writers during the scan, and the `list(...)` snapshot keeps a disconnect mid-broadcast from breaking the loop. Background: [12_concurrency](../../12_concurrency/README.md).

---

## Your 11 Projects, as Story Material

Every project doubles as an interview story. No job history yet? These count.

| Project | Angle for a story |
|---------|-------------------|
| [01 Calculator](../../Projects/01_calculator/README.md) | First ship. Debugging divide-by-zero and invalid-input edge cases |
| [02 Todo App](../../Projects/02_todo_app/README.md) | What if the save file is corrupt? Designing for bad data |
| [03 File Organizer](../../Projects/03_file_organizer/README.md) | Safety: moving files without ever destroying one; logging decisions |
| [04 Data Analyzer](../../Projects/04_data_analyzer/README.md) | Messy real-world data; reporting honestly instead of guessing |
| [05 Quiz Game](../../Projects/05_quiz_game/README.md) | Scope creep — categories, timers, leaderboards — and shipping in slices |
| [06 Personal Journal](../../Projects/06_personal_journal/README.md) | Privacy by design; text-encoding surprises when exporting |
| [07 Password Manager](../../Projects/07_password_manager/README.md) | Security mindset, and knowing your tool's limits (its README says so itself) |
| [08 URL Shortener](../../Projects/08_url_shortener/README.md) | Design trade-offs: generating short codes without collisions |
| [09 Chat Server](../../Projects/09_chat_server/README.md) | The concurrency bug above: shared state, locks, intermittent failures |
| [10 Static Site Generator](../../Projects/10_static_site_generator/README.md) | Pipeline thinking: content → templates → output, rebuilt end to end |
| [11 Tic-Tac-Toe AI](../../Projects/11_tic_tac_toe_ai/README.md) | Debugging a wrong answer: "why did the AI play badly?" → trace the recursion |

The full overview lives in [Projects/README.md](../../Projects/README.md).

---

## Questions You Should Be Ready For

Practice out loud — STAR collapses the first few times you say it.

- **"Tell me about a bug you fixed."** The chat server story above fits perfectly.
- **"A time you had to learn something fast."** Threads and sockets for the chat
  server, or minimax for tic-tac-toe — from "no idea" to "shipped it."
- **"Why Python?"** Have a real answer — readable first, batteries-included stdlib:
  servers, file tools, and tests, with no installs.
- **"Tell me about a project you're proud of."** Pick one from the table, not three.
- **"How do you handle getting stuck?"** Concrete beats noble: re-read the traceback,
  shrink the input, explain the code line by line — habits from [14_debugging](../../14_debugging/README.md).

---

## Good Questions for *You* to Ask

Interviewers nearly always end with "any questions for us?" — have two or three ready:

- "What would a typical first project look like for someone in this role?"
- "How does code review work here — how do people give and receive feedback?"
- "What is the team struggling with most right now?"
- "How is success measured in the first three months?"

Avoid leading with salary in a first-round technical chat — that conversation is for after they want you.

---

## Anti-Patterns

- **Trash-talking past work, teachers, or employers.** It reads as "will talk about
  us the same way." Reframe negatives as what you'd do differently now.
- **Bluffing.** Don't claim knowledge you don't have — it fails the follow-up. Say
  how you'd find out instead: *"I haven't used X yet — I'd read the docs, then
  write a two-line test script to see what it actually does."*
- **Oversharing.** Keep STAR answers around two minutes, and keep medical, legal,
  and salary-frustration stories out entirely. Be warm, not confessional.

---

## One More Story: This Site Itself

[ROADMAP.md](../../ROADMAP.md) lays out an 18-week, seven-stage path from "hello world" to advanced concepts.
If you've followed it — or are partway through — *that* is a self-taught learning story: no teacher, no
deadline, you kept going. "Tell me about a time you learned something on your own" writes itself.

---

## Keep Going

- Answers land harder when the skills behind them are real — the module READMEs and [quizzes](../quizzes.md) are your proof-of-work.
- For tools beyond this site's stdlib-only scope (pytest, requests, real password hashing), see [further_reading.md](../further_reading.md).
- Back to the [Resources index](../README.md).
