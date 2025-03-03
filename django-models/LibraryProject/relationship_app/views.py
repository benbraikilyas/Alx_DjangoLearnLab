class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ تأكد من تحديد القالب بشكل صحيح
    context_object_name = "library"
