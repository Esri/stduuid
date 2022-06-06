from conans import ConanFile


class StdUUIDConan(ConanFile):
    name = "stduuid"
    version = "1.2.2"
    url = "https://github.com/Esri/stduuid"
    license = "https://github.com/Esri/stduuid/blob/master/LICENSE"
    description = "A C++17 cross-platform single-header library implementation for universally unique identifiers"

    # RTC specific triple
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/stduuid/"

        # headers
        self.copy("uuid.h", src=base + "include", dst=relative + "stduuid")

        # no libraries; header-only
