from .base import BaseHighlighter

class SqlHighlighter(BaseHighlighter):
    KEYWORDS = [
        "SELECT", "INSERT", "UPDATE", "DELETE", "FROM", "WHERE", "AND", "OR", "NOT", "NULL", "IS", "IN",
        "BETWEEN", "LIKE", "JOIN", "INNER", "LEFT", "RIGHT", "FULL", "ON", "AS", "ORDER", "BY", "GROUP",
        "HAVING", "DISTINCT", "CREATE", "ALTER", "DROP", "TABLE", "DATABASE", "VIEW", "INDEX", "PRIMARY",
        "KEY", "FOREIGN", "REFERENCES", "UNIQUE", "CHECK", "DEFAULT", "VALUES", "SET", "LIMIT", "OFFSET",
        "UNION", "ALL", "EXISTS", "CASE", "WHEN", "THEN", "ELSE", "END"
    ]
    COLOR = "#800080"
